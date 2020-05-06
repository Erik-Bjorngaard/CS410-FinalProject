//click category menu
$(".btn").click(function() {
  hideshow($(this));
});

//close button
$(".close-button").click(function() {
  hideshow($($(this).data("target")));
});

//certain jumps between sections
$(".jump").click(function() {
  hideshow($($(this).data("target")));
  $('html, body').animate({scrollTop: $(".category").offset().top}, 200);
});

//back top
$("#to-top").click(function() {
  $('html, body').animate({scrollTop: 0}, 500);
});


function hideshow(x) {
  if($(".content-container").hasClass('active')) {
    if($(x.data("target")).hasClass('active')) {
        $(x.data("target")).removeClass('active');
        $(".content-container").removeClass('active');
        x.removeClass('highlight');
    }
    
    else{
      $(".content-container").children().removeClass('active');
      $(x.data("target")).addClass('active');
      $(".btn").removeClass('highlight');
      x.addClass('highlight');
    }
  }

  else {
    $(".content-container").addClass('active');
    $(x.data("target")).addClass('active');
    x.addClass('highlight');
  }
}
