var infoMode = 0;
var imgMode = 0;

$(document).ready(function() {
    $(".pkmn-d").hide();
    $(".pkmn-d2").hide();
    $(".sprite-s").hide();

    $("#info-mode").click(function() {
        if (infoMode == 0){ // switch to defense
            $("#info-mode").html("Defending");
            $(".pkmn-a").hide();
            $(".pkmn-a2").hide();
            $(".pkmn-d").show();
            $(".pkmn-d2").show();
            infoMode = 1;

        }else{              // switch to offense
            $("#info-mode").html("Attacking");
            $(".pkmn-a").show();
            $(".pkmn-a2").show();
            $(".pkmn-d").hide();
            $(".pkmn-d2").hide();
            infoMode = 0;
        }
    });
    $("#img-mode").click(function() {
        if (imgMode == 0){ // switch to shiny
            $("#img-mode").html("Shiny Sprites");
            $(".sprite-s").show();
            $(".sprite").hide();
            imgMode = 1;

        }else{              // switch to regular
            $("#img-mode").html("Normal Sprites");
            $(".sprite-s").hide();
            $(".sprite").show();
            imgMode = 0;
        }
    });
  });