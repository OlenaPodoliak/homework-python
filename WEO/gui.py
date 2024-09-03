import FreeSimpleGUI as sg
inputTest = sg.Text("Choose the file to compare:")
inputTest1 = sg.Text("File 1:")
input1 = sg.Input(key = "file1", size=(60,1), font=("Courier New",10))
choose_button1 = sg.FileBrowse("Choose", key="btnFile1")

inputTest2 = sg.Text("File 2:")
input2 = sg.Input(key = "file2", size=(60,1), font=("Courier New",10))
choose_button2 = sg.FileBrowse("Choose", key="btnFile2")

compare_button = sg.Button("Compare", key="btnCompare")
window = sg.Window("Comparing",
                [[inputTest],
                 [inputTest1, input1, choose_button1],
                 [inputTest2, input2, choose_button2],
                 [compare_button]
                 ],
                font=("Arial",12))
while True:
    event, values = window.read()
    match event:
        case "btnCompare":
            print(event,values["file1"])
        case sg.WIN_CLOSED:
            break

window.close()
