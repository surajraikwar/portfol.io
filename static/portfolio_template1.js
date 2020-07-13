(function ($) {

  // Variables
  let $project = $('.project'),
  $projects = $('.projects'),
  $projectCircleBefore = CSSRulePlugin.getRule('.project__graphics:before'),
  $projectCircleAfter = CSSRulePlugin.getRule('.project__graphics:after');

  // Main project timeline
  let tlProjects = new TimelineMax();
  tlProjects.
  set($projects, { autoAlpha: 1 });

  // Individual project timeline
  let tlProject = new TimelineMax({ repeat: 3, repeatDelay: 2 });

  $project.each(function (index, element) {
    let $this = $(this);

    // General Project Items
    let projectClasses = $this.attr('class').split(' '),
    themeClass = projectClasses[1],
    $loader = $this.find('.project__loader'),
    $pixel = $this.find('.pixel'),
    $pixelContainer = $this.find('.pixel-container'),
    $projectTitle = $this.find('.project__title'),
    $projectSubtitle = $this.find('.project__subtitle'),
    $projectGraphics = $this.find('.project__graphics');

    // Project CTA Timeline and Items
    let tlProjectsCTA = new TimelineMax(),
    $projectLink = $this.find('.button-container'),
    $projectLinkButton = $this.find('.button'),
    $projectLinkParts = $this.find('.button__part'),
    $projectLinkText = $this.find('.button__text');

    tlProjectsCTA.
    to($projectSubtitle, 0.3, { autoAlpha: 0, yPercent: 100, ease: Back.easeOut }).
    staggerFrom($projectLinkParts, 0.3, { autoAlpha: 0, yPercent: -100, ease: Back.easeOut }, 0.1).
    from($projectLinkText, 0.3, { autoAlpha: 0, x: '-100%', ease: Power4.easeInOut }, '-=0.2');

    // Project Loader Timeline
    let tlProjectLoader = new TimelineMax({ paused: true });

    tlProjectLoader.
    to([$projectCircleBefore, $projectCircleAfter], 0.4, { cssRule: { opacity: '0' } }).
    fromTo($loader, 5, { strokeDasharray: 547, strokeDashoffset: 547 }, { strokeDasharray: 547, strokeDashoffset: 0, ease: Power0.easeNone }).
    to($loader, 0.4, { autoAlpha: 0, onComplete: resumeProjects }).
    to([$projectCircleBefore, $projectCircleAfter], 0.4, { cssRule: { opacity: '1' } }, '-=0.4');

    // Create a project timeline
    tlProject.
    set($(this), { zIndex: 1 }).
    set([$projectTitle, $projectSubtitle, $pixel], { autoAlpha: 0 }).
    fromTo($projectGraphics, 0.4, { autoAlpha: 0, xPercent: '-200' }, { autoAlpha: 1, xPercent: '-10', ease: Power4.easeInOut, onStart: updateClass, onStartParams: [themeClass] }).
    add('imageIn').
    staggerFromTo($pixel, 0.3, { autoAlpha: 0, x: '-=10' }, { autoAlpha: 1, x: '0', ease: Power4.easeInOut }, 0.02, '-=0.2').
    add('pixelsIn').
    fromTo($projectTitle, 0.7, { autoAlpha: 0, xPercent: '-50' }, { autoAlpha: 1, xPercent: '-5', ease: Power4.easeInOut }, '-=0.4').
    fromTo($projectSubtitle, 0.7, { autoAlpha: 0, xPercent: '-50' }, { autoAlpha: 1, xPercent: '-2', ease: Power4.easeInOut }, '-=0.5').
    add('titleIn').
    add(tlProjectsCTA, '+=2') // add button animation to the project timeline
    .to($projectTitle, 4.3, { xPercent: '+=5', ease: Linear.easeNone }, 'titleIn-=0.1').
    to($projectSubtitle, 4.3, { xPercent: '+=2', ease: Linear.easeNone }, 'titleIn-=0.2').
    add('titleOut').
    to($projectGraphics, 5, { xPercent: '0', ease: Linear.easeNone, onComplete: pauseProjects, onCompleteParams: [themeClass, tlProjectLoader] }, 'imageIn').
    add('imageOut').
    to($pixelContainer, 4.1, { x: '5', ease: Linear.easeNone }, 'pixelsIn').
    to([$projectTitle, $projectSubtitle, $projectLink], 0.5, { autoAlpha: 0, xPercent: '+=10', ease: Power4.easeInOut }, 'titleOut').
    to($projectGraphics, 0.4, { autoAlpha: 0, xPercent: '+=80', ease: Power4.easeInOut }, 'imageOut');

    // Add project to the master projects timeline
    tlProjects.add(tlProject);
  });

  // Circles rotation timeline
  let tlCircles = new TimelineMax({ repeat: -1 });

  tlCircles.
  to($projectCircleBefore, 0.8, { cssRule: { top: '5px' }, ease: Linear.easeNone }).
  to($projectCircleBefore, 0.8, { cssRule: { left: '5px' }, ease: Linear.easeNone }).
  to($projectCircleBefore, 0.8, { cssRule: { top: '-5px' }, ease: Linear.easeNone }).
  to($projectCircleBefore, 0.8, { cssRule: { left: '-5px' }, ease: Linear.easeNone }).
  to($projectCircleAfter, 0.7, { cssRule: { bottom: '6px' }, ease: Linear.easeNone }, '0.0').
  to($projectCircleAfter, 0.7, { cssRule: { right: '6px' }, ease: Linear.easeNone }, '0.7').
  to($projectCircleAfter, 0.7, { cssRule: { bottom: '-6px' }, ease: Linear.easeNone }, '1.4').
  to($projectCircleAfter, 0.7, { cssRule: { right: '-6px' }, ease: Linear.easeNone }, '2.1');

  // Create a function to update the body class
  function updateClass(themeClass) {
    $('body').attr('class', `bg-${themeClass}`);
  }

  // Create a function to pause the project timeline
  function pauseProjects(themeClass, tlProjectLoader) {
    tlProjects.pause();

    if (themeClass !== 'theme-00') {
      tlProjectLoader.seek(0);
      tlProjectLoader.play();
    }
  }

  // Create a functino to resume projects
  function resumeProjects() {
    tlProjects.resume();
  }

  // Starts the projects timeline on click
  $('.js-view-projects').on('click', function (event) {
    event.preventDefault();
    tlProjects.resume();
  });
})(jQuery);