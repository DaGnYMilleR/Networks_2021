package com.company.commands;

import org.eclipse.egit.github.core.Repository;
import org.eclipse.egit.github.core.service.RepositoryService;

import java.io.IOException;
import java.io.PrintStream;

public class RepositoryInfoCommand extends Command{
    @Override
    public String getName() {
        return "repinf";
    }

    @Override
    public void execute(String[] args, PrintStream writer){
        validate(args);
        try {
            var repository = new RepositoryService().getRepository(args[0], args[1]);
            writer.println(formatRepositoryInfo(repository));
        } catch (IOException e) {
            writer.println("something went wrong at " + getName() + "command");
        }
    }

    private void validate(String[] args) {
        if(args == null || args.length != 2)
            throw new ArithmeticException("wrong arguments count");
    }

    private String formatRepositoryInfo(Repository repository) {
        var builder = new StringBuilder();
        builder.append("Name: ").append(repository.getName()).append("\n");
        builder.append("Created at: ").append(repository.getCreatedAt().toString()).append("\n");
        builder.append("Forks: ").append(repository.getForks()).append("\n");
        if (repository.getDescription() != null && !repository.getDescription().isEmpty())
            builder.append("Description: ").append(repository.getDescription()).append("\n");
        builder.append("Languages: ").append(repository.getLanguage()).append("\n");
        builder.append("Size: ").append(repository.getSize()).append("MB").append("\n");
/*        try {
            builder.append("Contributors: ").append(getContributors(new RepositoryService().getContributors(repository, true).toArray()));
        } catch (IOException e) {
            e.printStackTrace();
        }*/
        return builder.toString();
    }

/*    private static String getContributors(Object[] contributors){
        return contributors.stream().map(Contributor::getLogin).filter(Objects::nonNull).collect(Collectors.joining(", "));
    }*/
}
