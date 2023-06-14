package Homework25.view;

import java.util.ArrayList;
import java.util.List;

import Homework25.view.commands.CreateFile;
import Homework25.view.commands.Exit;
import Homework25.view.commands.OpenFile;
import Homework25.view.commands.WorkWithFile;

import java.io.IOException;
import java.lang.StackWalker.Option;

public class Menu {
    private List<Option> commands;
    private Console console;

    public Menu(Console console){
        this.console = console;
        commands = new ArrayList<>();
        commands.add(new CreateFile(console));
        commands.add(new OpenFile(console));
        commands.add(new Exit(console));

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
