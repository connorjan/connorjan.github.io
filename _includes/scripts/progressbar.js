//capture scroll any percentage
// $(window).scroll(
// 	function() {
// 		var wintop = $(window).scrollTop(),docheight = $(document).height(),winheight =$(window).scrollTop();
// 		var scrolled = (wintop/(docheight-winheight))*100;
// 		$('.progress-bar').css('width', (scrolled + '%'));
// 	}
// );

// (function(document) {
// 	document.addEventListener('scroll', function(s) {
// 					var wintop = $(window).scrollTop(),docheight = $(document).height(),winheight =$(window).scrollTop();
// 					var scrolled = (wintop/(docheight-winheight))*100;
// 					$('.progress-bar').css('width', (scrolled + '%'));
// 				}, false);
// })(document);


window.onscroll = function() {modifyScroll()};

function modifyScroll() {
	var wintop = $(window).scrollTop(), docheight = $(document).height(), winheight = $(window).scrollTop();
	var scrolled = (wintop/(docheight-winheight))*100;
	$('.progress-bar').css('width', (scrolled + '%'));
};
