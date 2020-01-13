$(document).ready(function() {

    var table = $('#table');

    // Table bordered
    $('#table-bordered').change(function() {
        var value = $(this).val();
        table.removeClass('table-bordered').addClass(value);
    });

    // Table striped
    $('#table-striped').change(function() {
        var value = $(this).val();
        table.removeClass('table-striped').addClass(value);
    });

    // Table hover
    $('#table-hover').change(function() {
        var value = $(this).val();
        table.removeClass('table-hover').addClass(value);
    });

    // Table color
    $('#table-color').change(function() {
        var value = $(this).val();
        table.removeClass(/^table-mc-/).addClass(value);
    });
});

(function(removeClass) {

    jQuery.fn.removeClass = function(value) {
        if (value && typeof value.test === "function") {
            for (var i = 0, l = this.length; i < l; i++) {
                var elem = this[i];
                if (elem.nodeType === 1 && elem.className) {
                    var classNames = elem.className.split(/\s+/);

                    for (var n = classNames.length; n--;) {
                        if (value.test(classNames[n])) {
                            classNames.splice(n, 1);
                        }
                    }
                    elem.className = jQuery.trim(classNames.join(" "));
                }
            }
        } else {
            removeClass.call(this, value);
        }
        return this;
    }

})(jQuery.fn.removeClass);

$('select').on('change', function() {
    // console.log('season:', this.value);
    // Get Stat
    $.ajax({
        url: "/api/stat?season="+this.value,
        contentType : "application/json",
        dataType: "json",
        type: 'get',
        success: function(result) {
            if(result.success == true) {
                console.log('Result fetched');
                console.log('result:', result.data);
                Object.keys(result.data).forEach(function(key) {
                    if(key == 'winner_teams') {
                        let winningTeams = ''
                        Object.keys(result.data[key]).forEach(function(key2) {
                            if(winningTeams.length == 0) {
                                winningTeams = result.data[key][key2]['winner']
                            }
                            else {
                                winningTeams = winningTeams+', '+result.data[key][key2]['winner']
                            }
                            $('#winning-teams').html(winningTeams)
                        })
                    }
                    else if (key == 'most_toss') {
                        $('#most-toss').html(result.data[key])
                    }
                    else if (key == 'most_player_of_match') {
                        $('#most-player-of-match').html(result.data[key])
                    }
                    else if (key == 'most_match_winning_team') {
                        $('#most-match-winning-team').html(result.data[key])
                    }
                    else if (key == 'most_winning_team_city') {
                        $('#most-winning-team-city').html(result.data[key])
                    }
                    else if (key == 'toss_bat_percent') {
                        $('#toss-bat-percent').html(result.data[key])
                    }
                    else if (key == 'city_based') {
                        $('#city-based').html(result.data[key]['total_games'][0]['city'])
                    }
                    else if (key == 'largest_run_winners') {
                        $('#largest-run-winners').html(result.data[key])
                    }
                    else if (key == 'highest_wicket_winners') {
                        $('#highest-wicket-winners').html(result.data[key])
                    }
                    else if (key == 'team_win_toss_match') {
                        $('#team-win-toss-match').html(result.data[key]['total_teams'])
                    }
                });
            }
            else {
                console.log('Something went wrong! Contact Admin');
            }
        },
        error: function(error) {
            console.log('error:', error);
            // console.log('error message:', error.responseJSON.errors[0].message);
        }
    });
});
