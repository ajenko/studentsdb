// Journal 
// ------------------------------------------------------------------------

function initJournal() {
	var indicator = $('#ajax-progress-indicator');

	$('.day-box input[type="checkbox"]').click(function(event){
		var box = $(this);
		$.ajax(box.data('url'), {
			'type': 'POST',
			'async': true,
			'dataType': 'json',
			'data': {
				'pk': box.data('student-id'),
				'date': box.data('date'),
				'present': box.is(':checked') ? '1': '',
				'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
			},
			'beforeSend': function(xhr, settings){
				indicator.show();
			},
			'error': function(xhr, status, error) {
				alert(error);
				indicator.hide();
			},
			'success': function(data, status, xhr){
				indicator.hide();
			}
		});
	});
}

// Group selector 
// ------------------------------------------------------------------------

function initGroupSelector() {
	// look up select element with groups and attach our even handler 
	// on field 'change' event 
	$('#group-selector select').change(function(event){
		// get value of currently selected group option
		var group = $(this).val();

		if (group) {
			// set cookie with expiration date 1 year since now;
			// cookie creation function takes period in days 
			$.cookie('current_group', group, {'path': '/', 'expires': 365});

		} else {
			// otherwise we delete the cookie 
			$.removeCookie('current_group', {'path': '/'});

		}
		// and reload a page
		location.reload(true);

	});
}

// Date and time picker 
// ------------------------------------------------------------------------

function initDateAndTimeFields() {
	$('input.dateinput').datetimepicker({
		'format': 'YYYY-MM-DD',
		'locale': 'uk'
	});
	$('#birthday').datetimepicker({
		'format': 'YYYY-MM-DD',
		'locale': 'uk'
	});
	$('#date_time_exam').datetimepicker({
		'format': 'YYYY-MM-DD HH:MM:SS',
		'locale': 'uk'
	});
	$('#date_time').datetimepicker({
		'format': 'YYYY-MM-DD HH:MM:SS',
		'locale': 'uk'
	});
}

// Groups
// ------------------------------------------------------------------------

function initAddGroupPage() {
	$('a#group-add-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dateType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got a successfull response from the server
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}

				// update modal window with an arrived content from the server 
				var modal = $('#myModal');
				var html = $(data);
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our add form
				initForm(form, modal);
				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true

				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

function initEditGroupPage() {
	$('li a.group-edit-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dateType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got a successfull response from the server
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}

				// update modal window with an arrived content from the server 
				var modal = $('#myModal');
				var html = $(data);
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our add form
				initForm(form, modal);
				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true

				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

function initDeleteGroupPage() {
	$('li a.group-delete-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dateType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got a successfull response from the server
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}

				// update modal window with an arrived content from the server 
				var modal = $('#myModal');
				var html = $(data);
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our add form
				initForm(form, modal);
				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true

				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

// Students
// ------------------------------------------------------------------------

function initAddStudentPage() {
	$('a#student-add-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dateType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got a successfull response from the server
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}

				// update modal window with an arrived content from the server 
				var modal = $('#myModal');
				var html = $(data);
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our add form
				initForm(form, modal);
				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true

				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}


function initEditStudentPage() {
	$('a.student-edit-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we`ve got a successfull response form the server
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}
				// update modal window with arrived content from the server
				var modal = $('#myModal'), html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our form 
				initForm(form, modal);
			

				// setup and show modal window finally 
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true		
				});
			},
			'error' : function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

function initDeleteStudent() {
	$('a.student-delete-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we`ve got a successfull response form the server
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}
				// update modal window with arrived content from the server
				var modal = $('#myModal'), html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our form 
				initForm(form, modal);
			

				// setup and show modal window finally 
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true		
				});
			},
			'error' : function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

function initForm(form, modal) {
	// attach datetimepicker
	initDateAndTimeFields()

	// close modal window in Cancel button click 
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;
	});

	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert(gettext('There was an error on the server. Please, try againg a bit later.'));
			return false;
		},
		'success': function(data, status, xhr) {
			var html = $(data), newform = html.find('#content-column form');

			// copy alert to modal window
			modal.find('.modal-body').html(html.find('.alert'));

			// copy form to modal if we found it in server response
			if (newform.length > 0) {
				modal.find('.modal-body').append(newform);

				// initialize form fields and buttons
				initForm(newform, modal);
			} else {
				// if no form, it means success and we need to reload page
				// to get update students list;
				// reload after 2 seconds, so that user can read
				// success message
				setTimeout(function(){location.reload(true);}, 500);
			}
		
		}
	});
}

// Exams 
// ------------------------------------------------------------------------
function initAddExam() {
	$('a#exam-add-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got successfull response from the server 
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}
				// update modal window with arrived content from the server
				var modal = $('#myModal')
				var html = $(data)
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our form 
				initForm(form, modal);
			

				// setup and show modal window finally 
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true		
				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

function initEditExam() {
	$('li a.exam-edit-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got successfull response from the server 
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}
				// update modal window with arrived content from the server
				var modal = $('#myModal')
				var html = $(data)
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our form 
				initForm(form, modal);
			

				// setup and show modal window finally 
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true		
				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

function initDeleteExam() {
	$('li a.exam-delete-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got successfull response from the server 
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}
				// update modal window with arrived content from the server
				var modal = $('#myModal')
				var html = $(data)
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our form 
				initForm(form, modal);
			

				// setup and show modal window finally 
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true		
				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

// Ratings
// ------------------------------------------------------------------------
function initAddRating() {
	$('a#rating-add-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got successfull response from the server 
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}
				// update modal window with arrived content from the server
				var modal = $('#myModal')
				var html = $(data)
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our form 
				initForm(form, modal);
			

				// setup and show modal window finally 
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true		
				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

function initEditRating() {
	$('li a.rating-edit-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got successfull response from the server 
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}
				// update modal window with arrived content from the server
				var modal = $('#myModal')
				var html = $(data)
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our form 
				initForm(form, modal);
			

				// setup and show modal window finally 
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true		
				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}

function initDeleteRating() {
	$('li a.rating-delete-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got successfull response from the server 
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}
				// update modal window with arrived content from the server
				var modal = $('#myModal')
				var html = $(data)
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our form 
				initForm(form, modal);
			

				// setup and show modal window finally 
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true		
				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}
// Contact with Admin
// ------------------------------------------------------------------------
function initContactAdmin() {
	$('li a#admin-add-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr){
				// check if we got successfull response from the server 
				if (status != 'success') {
					alert(gettext('There was an error on the server. Please, try againg a bit later.'));
					return false;
				}
				// update modal window with arrived content from the server
				var modal = $('#myModal')
				var html = $(data)
				var form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our form 
				initForm(form, modal);
			

				// setup and show modal window finally 
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true		
				});
			},
			'error': function(){
				alert(gettext('There was an error on the server. Please, try againg a bit later.'));
				return false;
			}
		});
		return false;
	});
}
// Set Language
// ------------------------------------------------------------------------


function setLang(){
	$('.lang').change(function(event){
		var lang = $(this);
		$.ajax(lang.data('url'), {
			'type': 'GET',
			'async': true,
			'dataType': 'json',
			'beforeSend': function(xhr, setting) {

			},
			'error': function(xhr, status, error) {
				alert('error');

			},
			'success': function(data, status, xhr) {
				$.cookie(data.django_lang, lang.attr('value'), {'path': '/', 'expires': 365});
				location.reload(true);
			}

		});
		return true;
	});

}


$(document).ready(function(){
	initJournal();
	initGroupSelector();
	initDateAndTimeFields()
	initAddStudentPage();
	initEditStudentPage();
	initDeleteStudent();
	initAddGroupPage();
	initEditGroupPage();
	initDeleteGroupPage();
	initAddExam();
	initEditExam();
	initDeleteExam();
	initAddRating();
	initEditRating();
	initDeleteRating();
	initContactAdmin();

	setLang();



});
