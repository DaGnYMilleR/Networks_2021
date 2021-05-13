package com.company.commands;

import java.io.PrintStream;

public abstract class Command {
    public abstract String getName();

    public abstract void execute(String[] args, PrintStream writer);
}
