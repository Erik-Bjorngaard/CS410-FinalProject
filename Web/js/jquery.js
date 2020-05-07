// one selection for each checkbox category
$("input:checkbox").on('click', function() {
  var $box = $(this);
  if ($box.is(":checked")) {
    var group = "input:checkbox[name='" + $box.attr("name") + "']";
    $(group).prop("checked", false);
    $box.prop("checked", true);
  } 
  else {
    $box.prop("checked", false);
  }

});

// show result
function showResult() {
    var x = document.getElementById("result");
    x.style.display = "block";
}

// close button
$(".close-button").click(function() {
  hideshow($($(this).data("target")));
});

// back top
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
