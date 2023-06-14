package Homework25.view.commands;

import java.io.IOException;

import Homework25.view.Console;

public class Exit extends Command{

    public Exit(Console console) {
        super(console);
    }

    @Override
    public String descriptions() {
        return "Выйти";
    }

    @Override
    public void execute() throws IOException, ClassNotFoundException {
        getConsole().loadData();
    }
    
}
