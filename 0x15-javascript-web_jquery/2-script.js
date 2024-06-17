//updating color of header when user clicks a certain tag
$(document).ready(function () {
	$("DIV#red_header").click(function () {
		$("header").css("color", "#FF0000");
	});
});