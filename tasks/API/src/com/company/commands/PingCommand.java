package com.company.commands;

import java.io.PrintStream;

public class PingCommand extends Command{
    @Override
    public String getName() {
        return "ping";
    }

    @Override
    public void execute(String[] args, PrintStream writer) {
        writer.println("pong");
    }
}
