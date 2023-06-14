package Homework25.view.commands;

import java.io.IOException;

import Homework25.view.Console;

public class OpenFile extends Command{

    public OpenFile(Console console) {
        super(console);
    }

    @Override
    public String descriptions() {
        return "Открыть заметку";
    }

    @Override
    public void execute() throws IOException, ClassNotFoundException {
        getConsole().loadData();
    }
    
}
