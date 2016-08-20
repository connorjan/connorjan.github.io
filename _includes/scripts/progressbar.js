
// Scroll bar!
(function(document) {
	document.addEventListener('scroll', function(s) {
					var wintop = $(window).scrollTop(),docheight = $(document).height(),winheight =$(window).scrollTop();
					var scrolled = (wintop/(docheight-winheight))*100;
					$('.progress-bar').css('width', (scrolled + '%'));
				}, false);
})(document);