
makeChecklist();
fetchTestListData();

var myData2 = {};
function fetchTestListData() {

       var request = $.ajax({
            url: 'http://localhost:8080/tests',
            jsonp: "GetStationTests",
            type: 'GET',
        });

        request.done( function(data) {
            console.log(data);
            myData2 = data;
        });


        request.error( function() {
            console.log("Ajax request error");
        });

}


function makeChecklist(){

    var myData =
        {
            tests_stress_testing: [ ],
            tests_power_states: [ ],
            tests_aux: [
                "AuxWithPowerCycle",
                "AuxToDiscoverableWith_BTButton",
                "Button_MFBAtAUXToFD",
                "StandbyIgnoreBlueToothPair",
                "AuxToConnectingState",
                "vol",
                "AuxToDiscoverableWithEmptyList",
                "AuxToDiscoverableWithClearList_BTButton",
                "AuxToStandby",
                "AuxInactiveToStandby",
                "StandbyToAux"
            ],
            tests_hfp: [ ],
            tests_ipc: [
                "Venom_HighTemp"
            ],
            tests_update_dut: [
                "discoverableToUpdate"
            ],
            tests_bt_connectivity: [
                "discoverableWithEmptyPairingList",
                "Bluetooth_List_Clear_to_Discoverable",
                "BTInactivelyToStandby",
                "discoverableWithClearPairingList",
                "Main_ConnectingToDiscoverableWithPHBluetooth",
                "discoverableWithRestartInactivityTimer",
                "Main_ConnectedToConnecting",
                "discoverableToConnecting",
                "StandbyToDiscoverable",
                "StandbyToConnect"
            ],
            tests_bt_audio: [
                "audioPlayPause",
                "VolumePersistsPowerCycle"
            ]
            };

function makeChecklist(){

}
    var $category_list = $("#myCheckList");

    for (var test_cat in myData) {
        if (myData.hasOwnProperty(test_cat)) {
            $category_list.append('<input type="checkbox" class="tests" value="success" id="' + test_cat + '">' +
                                   '<label for=' + test_cat + '>'+test_cat+'</label> <br>');
        }
    }
    $category_list.append('<input type = "submit" value="Submit" id="test-submit" onclick="getSelectedTests()">')
}


function getSelectedTests(){
    test_array = [];
        $('.tests').each(function(){
            if($(this).is('input:checked'))
            {
                //test_array.push({test:$(this).attr('id')});
                test_array.push({test:$(this).attr('id')});
                //alert($(this).attr('id'))
            }
        });
        alert(JSON.stringify(test_array));
}


            /*
            $category_list.append("<li class='test-category'>" + test_cat +"</li>");

            var current_cat = myData[test_cat];

            if (current_cat.length > 0) {
              var category = $category_list.append("<li class='test-category'>" + test_cat +"</li>");
              //$(".test-category").append("<ul></ul>");
              console.log($category_list)
              var $test_list = $category.append("<ul>hello</ul>")
             // var $test_list = $("#test-"+ test_cat).append("<ul id=" + test_cat+ "></ul>")

              for(var i=0; current_cat.length > i ; i++) {
                //console.log(current_cat[i]);
                //$(".subCheckList").append("<li class='sub-test-category'>" + current_cat[i] + "</li>");
               // $test_list.append("<li class='sub-test-category'>" + current_cat[i] + "</li>");
              }
            } else {
                continue;
            }*/




