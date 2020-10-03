odoo.define('interview_test.portalpages', function (require) {
	'use strict';
	console.log('haiipageformwebsite');
	$(document).ready(function () {

	$(".js-example-placeholder-single").select2({
    placeholder: "Select  customer"

		});


	 $("#cutomers").on('change', function () {
	  var postid = $("#cutomers").val();
	 	 console.log(postid);
	 	 $("#partnercode").val(postid);


		});


	 });
});
