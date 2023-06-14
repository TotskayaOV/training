package Homework25.view.commands;

import java.io.IOException;

public interface Option {
    String descriptions();
    void execute() throws IOException, ClassNotFoundException;
    
}
