package com.company;

import com.company.commands.Command;

import javax.swing.*;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;
import java.util.function.Function;

public class CommandsExecutor {
    private final PrintStream writer;
    private ArrayList<Command> commands = new ArrayList<>();

    public CommandsExecutor(PrintStream writer){
        this.writer = writer;
    }

    public void registerCommand(Command command){
        commands.add(command);
    }

    public void execute(String[] args){
        if (args[0].length() == 0)
        {
            writer.println("Please specify <command> as the first command line argument");
            return;
        }

        var commandName = args[0];
        var cmd = findCommandByName(commandName);
        if (cmd == null)
            writer.println("Sorry. Unknown command " + commandName);
        else
            cmd.execute(Arrays.stream(args).skip(1).toArray(String[]::new), writer);
    }

    private Command findCommandByName(String name){
        return commands.stream()
                .filter((x) -> x.getName().equals(name))
                .findFirst()
                .orElse(null);
    }
}
