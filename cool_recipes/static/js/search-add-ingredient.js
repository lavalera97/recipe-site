$(document).ready(function() {
    var max_fields      = 4; //maximum input boxes allowed
    var wrapper         = $(".input_fields_wrap"); //Fields wrapper
    var add_button      = $(".add_field_button"); //Add button ID
    var ingredient_number = 1

    var x = 1; //initial text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row delete-row" style="padding-top: 15px;"><div class="col-lg-8 col-md-10 col-sm-9"><input type="text" placeholder="Ингредиент" class="form-control" name="ingredient_name['+ ingredient_number +']"></div><div class="col-lg-1 col-md-2 col-sm-3 add-button-div"><button class="remove_field" type="button"><i class="fas fa-minus" style="color:#D21B1B"></i></button></div>'); //add input box
            ingredient_number++;
        }
    });

    $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
        e.preventDefault(); $(this).closest('.delete-row').remove(); x--;
    })
});