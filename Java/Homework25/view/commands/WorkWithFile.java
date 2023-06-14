package Homework25.view.commands;

import java.io.IOException;

import Homework25.view.Console;
import java.io.IOException;

public class WorkWithFile extends Command{
    public WorkWithFile (Console console){
        super(console);

    }
    @Override
        public String descriptions(){
            return "Меню работы с файлом";
        }

    @Override
    public void execute() throws IOException, ClassNotFoundException{
        getConsole().loadData();
    }

}
