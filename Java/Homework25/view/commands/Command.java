package Homework25.view.commands;

import Homework25.view.Console;

public abstract class Command implements Option{
    private Console console;

    public Command(Console console) {
        this.console = console;
    }
    
    public Console getConsole() {
        return console;
    }

    // public abstract String description();
    // public abstract void execute();
}
