package Homework25.view.commands;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import Homework25.view.Console;

public class FileMenu {
    private List<Option> commands;
    private Console console;

    public FileMenu(Console console){
        this.console = console;
        commands = new ArrayList<>();
        commands.add(new WorkWithFile(console));

    }

    void execute (int num) throws IOException, ClassNotFoundException{
        Option option = commands.get(num);
        option.execute();
    }
    
    public String printMenu(){
        StringBuilder stringBuilder  = new StringBuilder();
        stringBuilder.append("\n")
        for (int i = 0; i < commands.size(); i++) {
            stringBuilder.append(i);
            stringBuilder.append(": ");
            stringBuilder.append(commands.get(i).descriptions());
            stringBuilder.append("\n");
        }
        return stringBuilder.toString();
    }

    public Integer getMenuRowsValue(){
        return commands.size();
    }
}
