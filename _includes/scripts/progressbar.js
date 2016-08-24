
// Scroll bar!

function getScrollPercent() {
    var h = document.documentElement, 
        b = document.body,
        st = 'scrollTop',
        sh = 'scrollHeight';
    return h[st]||b[st] / ((h[sh]||b[sh]) - h.clientHeight) * 100;
}

(function(document) {
	document.addEventListener('scroll', function(s) {
					//var scrollPercent = 100*($(window).scrollTop() / ($(document).height() - $(window).height()));
					$('.progress-bar').css('width', (getScrollPercent() + '%'));
				}, false);
})(document);