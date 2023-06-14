package Homework25.view;

import java.io.IOException;

import Homework25.presenter.Presenter;

public interface View {
    void setPresenter(Presenter presenter);
    void start() throws IOException, ClassNotFoundException;
    void print(String text);
}
