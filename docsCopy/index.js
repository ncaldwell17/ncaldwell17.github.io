/* exported raise_bar */
/* exported lower_bar */
/* exported activate */
/* exported loadvisual */
/* exported getData */
/* exported testData */
/* exported animatePolls */
/* exported fetch_mapData */
/* global document */
/* global window */ 


function raise_bar(count, type) {
    console.log(count)
    var res = type.charAt(0);
    document.getElementById("opt{0}{1}".format(count, res)).classList.add('pActive');
    if (count < 4) {
        count = count+1;
    } else {
        count = 4
    }
    console.log(count)
    return count;
}
    
function lower_bar(count, type) {
    window.console.log(count)
    var res = type.charAt(0);
    document.getElementById("opt{0}{1}".format(count, res)).classList.remove('pActive');
    if (count > 1) {
        count = count-1;
    } else {
        count = 1;
    }
    return count;
}

function flip(option, on, off, aToggle) {
    window.console.log("flip was used");
    if (option === 'off') {
        off.classList.add('active');
        on.classList.remove('active');
        aToggle.style.display = 'none';
    }
    if (option === 'on') {
        on.classList.add('active');
        off.classList.remove('active');
        aToggle.style.display = 'block';
    }
}

function otherflip(option, on, off) {
    if (option === 'off') {
        off.classList.add('active');
        on.classList.remove('active');
    }
    if (option === 'on') {
        on.classList.add('active');
        off.classList.remove('active');
    }
}

// First, checks if it isn't implemented yet.
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

function bool_it(condition) {
    if (condition === 'on') {
        return true;
    }
    else {
        return false;
    }
}

function get_lob_as_str(sw_array) {
    var map_string = [];
    for(var x in sw_array) {
        window.console.log(sw_array[x]);
        if(sw_array[x] === true) {
            var letter = "t";
        } 
        if(sw_array[x] === false) {
            letter = "f";
        }
        map_string.push(letter);
    }
    window.console.log(map_string);
    return map_string;
}

function determine_map(los) {
    var map_id = "url(images/{0}{1}{2}{3}{4}map.png)".format(los[0], los[1], los[2], los[3], los[4]);
    window.console.log(map_id);
    return map_id;
}

function fetch_mapData(switch1, switch2, switch3, switch4, switch5) {
    window.console.log(switch1, switch2, switch3, switch4, switch5);
    var map = document.getElementById('mapVisual');
    var map_switches = new Array(switch1, switch2, switch3, switch4, switch5);
    window.console.log(map_switches)
    var mapString = get_lob_as_str(map_switches);
    window.console.log(mapString);
    var mapID = determine_map(mapString);
    window.console.log(mapID);
    map.style.backgroundImage = mapID;
    window.console.log("completed fetch");
}

function activate(type, option) {
    var res = type.charAt(0);
    var onToggle = document.getElementById('{0}ToggleOn'.format(res));
    var offToggle = document.getElementById('{0}ToggleOff'.format(res));
    if (res == 'b' || res == 'o') {
        otherflip(option, onToggle, offToggle);
        var my_bool = bool_it(option);
        return my_bool;
    } 
    else {
        var myToggle = document.getElementById('{0}Percentile'.format(res));
        flip(option, onToggle, offToggle, myToggle);
        var my_bool2 = bool_it(option);
        return my_bool2;
    } 
}

function loadvisual() {
    document.getElementById('mapVisual').style.backgroundImage = 'url(images/optimized_risks.png)';
}

function getData() {
    window.console.log(o_switch, h_switch, s_switch, e_switch, c_switch);
    //store user's entry in a variable
    var enteredOutreach = document.getElementById('workers').value;
    var enteredRatio = document.getElementById('ratio').value;
    return [enteredOutreach, enteredRatio];  
    }

function testData(one, two) {
    console.log(one);
    console.log(two);
}