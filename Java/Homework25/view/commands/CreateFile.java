package Homework25.view.commands;

import java.io.IOException;

import Homework25.view.Console;

public class CreateFile extends Command{

    public CreateFile(Console console) {
        super(console);
    }

    @Override
    public String descriptions() {
        return "Создать заметку";
    }

    @Override
    public void execute() throws IOException, ClassNotFoundException {
        getConsole().loadData();
    }
    
}
