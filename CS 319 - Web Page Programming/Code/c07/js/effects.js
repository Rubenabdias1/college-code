$(function() {

  $('h2').hide().slideDown();
  var $h2 = $('h2')
  var $li = $('li');
  $li.hide().each(function(index) {
    $(this).delay(700 * index).fadeIn(700);
  });

  $li.on('click', function() {
    $(this).fadeOut(700);
  });

  $h2.on('click', function() {
    $(this).fadeOut(700);
  });
});