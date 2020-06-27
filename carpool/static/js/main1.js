
$(document).ready( function() {
function close() {
dialog.hide();
$('#add-user').focus();
}
var title = $('<h1>Add User</h1>').attr('id', 'add-user-title'),
closeButton = $('<button>close</button>')
.addClass('close')
.click(close)
.appendTo(title),
content = $('<div/>')
.load('add.html'),
dialog = $('<div/>')
.attr({
role: 'dialog',
'aria-labelledby': 'add-user-title'
})
.addClass('dialog')
.keypress(function(event) {
if (event.keyCode == 27) {
close();
}
})
.append(title)
.append(content)
.hide()
.appendTo('body');
$('#add-user').click(function() {
var height = dialog.height(),
width = dialog.width();
dialog
 .css({
 top: ($(window).height() - height) / 2
 + $(document).scrollTop(),
 left: ($(window).width() - width) / 2
+ $(document).scrollLeft()
})
.show();
dialog.find('#username').focus();
return false;
});
});
