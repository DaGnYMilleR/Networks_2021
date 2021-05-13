package com.company.commands;

import org.eclipse.egit.github.core.Repository;
import org.eclipse.egit.github.core.service.RepositoryService;

import java.io.IOException;
import java.io.PrintStream;

public class RepositoriesCommand extends Command{
    @Override
    public String getName() {
        return "allrepos";
    }

    @Override
    public void execute(String[] args, PrintStream printStream) {
        var count = 1;
        try {
            validate(args);
            try {
                for (Repository repo : new RepositoryService().getRepositories(args[0]))
                    printStream.println((formatMessage(count++, repo)));
            } catch (IOException e) {
                e.printStackTrace();
            }
        } catch (ArithmeticException e){
            printStream.println(e.getMessage());
        }
    }

    private void validate(String[] args) {
        if(args == null || args.length != 1)
            throw new ArithmeticException("wrong arguments count");
    }

    private String formatMessage(int count, Repository repository) {
        return count + ") " +
                repository.getName() +
                " - created on " +
                repository.getCreatedAt().toString();
    }
}
