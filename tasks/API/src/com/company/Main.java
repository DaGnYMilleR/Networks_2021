package com.company;

import java.util.Scanner;

import com.company.commands.PingCommand;
import com.company.commands.RepositoriesCommand;
import com.company.commands.RepositoryInfoCommand;
import org.eclipse.egit.github.core.Repository;
import org.eclipse.egit.github.core.service.RepositoryService;

public class Main {
    private static void RegisterCommands(CommandsExecutor executor){

        executor.registerCommand(new PingCommand());
        executor.registerCommand(new RepositoryInfoCommand());
        executor.registerCommand(new RepositoriesCommand());
    }


    public static void main(String[] args) {
        var executor = new CommandsExecutor(System.out);
        RegisterCommands(executor);

	    while (true){
	        System.out.print("> ");
            var scanner = new Scanner(System.in);
            var line = scanner.nextLine();
            if (line == null || line.equals("exit"))
                return;
            executor.execute(line.split(" "));
        }
    }
}
