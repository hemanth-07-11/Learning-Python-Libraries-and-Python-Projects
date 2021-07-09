import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow {
    id: mainWindow
    height: 160
    width: 300
    visible: true
    title: "My Window"

    Item {
        id: page
        visible: true

        width: parent.width

        Rectangle {
            id: myrectangle
            height: {
                console.log("writing like javascript")
                return 160
            }
            width: parent.width
            color: "#b2d2ed"

            Text{
                id: mainText
                text: "can type regular text"
                height: 50
                width: parent.width
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter

            }

            Button {
                id: mainbutton
                text: "Push Me"
                anchors.top: mainText.bottom
                anchors.horizontalCenter: mainText.bottom
                onClicked: {
                    if(myrectangle.color == "#b6b2ed"){
                        myrectangle.color = "#b2d2ed"
                    }else{
                        myrectangle.color = "#b6b2ed"
                    }
                    }

                }
            }
        }
        }

