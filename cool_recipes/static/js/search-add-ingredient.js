$(document).ready(function() {
    var wrapper         = $(".input-fields-wrap"); //Fields wrapper
    var add_button      = $(".add-field-button"); //Add button ID
    var ingredient_number = 1
    if ($(".create-recipe-field").length > 0) {
        var max_fields = 20;
    }
    else {
        var max_fields = 4;
    }

    var x = 1; //initial text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row delete-row" style="padding-top: 15px;"><div class="col-lg-8 col-md-10 col-sm-9"><input type="text" placeholder="Ингредиент" class="form-control" name="ingredient_name['+ ingredient_number +']"></div><div class="col-lg-1 col-md-2 col-sm-3 add-button-div"><button class="remove-field" type="button"><i class="fas fa-minus" style="color:#D21B1B"></i></button></div>'); //add input box
            ingredient_number++;
        }
    });

    $(wrapper).on("click",".remove-field", function(e){ //user click on remove text
        e.preventDefault(); $(this).closest('.delete-row').remove(); x--;
    })
});