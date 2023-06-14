package Homework25;

import Homework25.model.Notepad;
import Homework25.presenter.Presenter;
import Homework25.view.Console;
import Homework25.view.View;

public class Program {
    public static void main(String[] args) {
        View view = new Console();
        new Presenter(view, null);
        view.start();

        view.start();
    }
}