import java.io.*;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Todo {
    private static ArrayList<String> todoList = new ArrayList<String>();
    private static String toDoFileName = "todo.txt";
    private static String doneFileName = "done.txt";

    public static void main(String[] args) {
        final String commandHelp = "help";          //done
        final String commandAdd = "add";            //done
        final String commandDel = "del";            //done
        final String commandReport = "report";      //done
        final String commandDone = "done";
        final String commandLs = "ls";              //done

        if (args.length == 0 || commandHelp.equals(args[0])) {
            displayMenu();
        } else {
            switch (args[0]) {
                case commandAdd:
                    addItem(args);
                    break;
                case commandDel:
                    deleteItem(args);
                    break;
                case commandReport:
                    ReadFile();
                    break;
                case commandDone:
                    doneItem(args);
                    break;
                case commandLs:
                    showPending();
                    break;
            }
        }


    }

    static void displayMenu() {

        System.out.print("Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n" +
                "$ ./todo ls               # Show remaining todos\n" +
                "$ ./todo del NUMBER       # Delete a todo\n" +
                "$ ./todo done NUMBER      # Complete a todo\n" +
                "$ ./todo help             # Show usage\n" +
                "$ ./todo report           # Statistics");
    }

    /*Adding list item*/
    static void addItem(String[] args)  {
        try {
            if (args.length == 1) {
                System.out.println("Error: Missing todo string. Nothing added!");
            } else if (args.length == 2) {
                System.out.println("Added todo: " + "\"" + args[1] + "\"");
                //todoList.add(args[1]);
                appendToFile(args[1] + "\n");
            }
        }
        catch(Exception e){}

    }

    static void appendToFile(String message)  {
        try {
            FileWriter fw = new FileWriter(toDoFileName, true);
            fw.write(message);
            fw.close();
        } catch (Exception e) {

        }
    }

    static void ReadFile() {

        int ch;
        int Pending = 0;
        int Completed = 0;
        FileReader fr1 = null;
        FileReader fr2 = null;
        try {
            fr1 = new FileReader(toDoFileName);
            while ((ch = fr1.read()) != -1) {
                if (ch == '\n') {
                    Pending++;
                }
            }
            fr1.close();
        } catch (Exception fe) {

        }
        try {
            fr2 = new FileReader("done.txt");
            while ((ch = fr2.read()) != -1) {
                if (ch == '\n') {
                    Completed++;
                }
            }
            fr2.close();

        } catch (Exception e) {

        }



        generateReport(Pending, Completed);
    }

    static void showPending() {

        try {
            BufferedReader bufReader = new BufferedReader(new FileReader(toDoFileName));
            String line = bufReader.readLine();
            while (line != null) {
                todoList.add(line);
                line = bufReader.readLine();
            }
            bufReader.close();
            int reverseIndex = todoList.size() - 1;
            int reverseValue = todoList.size();
            while (reverseValue > 0) {
                System.out.println("[" + reverseValue + "]" + " " + todoList.get(reverseIndex));
                reverseIndex--;
                reverseValue--;
            }
        }
        catch(Exception e){}


    }

    static void doneItem(String[] args)  {
        try {
            if (args.length != 2) {
                System.out.println("Error: Missing NUMBER for deleting todo.");
                return;
            }
            int doneSelection = Integer.parseInt(args[1]);
            int doneIndex = doneSelection - 1;
            loadFileToList();
            int listSize = todoList.size();
            if (doneIndex > listSize) {
                System.out.println("Error: todo " + "#" + doneSelection + " does not exist.");
                return;
            }
            String message = "x " + getDate() + " " + todoList.get(doneIndex) + "\n";

            deleteItem(args);

            appendToDoneFile(message);
            System.out.println("Marked todo #" + doneSelection + " as done.");
        }
        catch(Exception e){}


    }

    static void appendToDoneFile(String message)   {
        try {
            FileWriter fw = new FileWriter(doneFileName, true);
            fw.write(message);
            fw.close();
        } catch (Exception e) {

        }
    }

    static void deleteItem(String[] args)  {
        todoList.clear();
        loadFileToList();

        System.out.println("size" + todoList.size());

        int deleteSelection = Integer.parseInt(args[1]);
        if (args.length != 2) {
            System.out.println("Error: Missing NUMBER for deleting todo.");
            return;
        }
        int listSize = todoList.size();

        int deleteIndex = deleteSelection - 1;
        System.out.println(deleteIndex);

        if (deleteIndex > listSize) {
            System.out.println("Error: todo " + "#" + deleteSelection + " does not exist.");
            return;
        }
        todoList.remove(deleteIndex);
        System.out.println("Deleted todo #" + deleteSelection);


        writeListToFile();

    }


    static void loadFileToList() {
        try {
            BufferedReader bufReader = new BufferedReader(new FileReader(toDoFileName));
            String line = bufReader.readLine();
            while (line != null) {
                todoList.add(line);
                line = bufReader.readLine();
            }
            bufReader.close();
        }
        catch(Exception e){}
    }

    static void writeListToFile()  {
        try {
            FileWriter writer = new FileWriter(toDoFileName, false);
            for (String str : todoList) {
                writer.write(str + "\n");
            }


            writer.close();
        }
        catch(Exception e){}
    }


    static void generateReport(int rem, int done) {
        String date = getDate();
        System.out.println(date + " " + "Pending : " + rem + " " + "Completed : " + done);

    }


    static void writeFileCompletedTasks(int a) {
        try {
            FileWriter fw = new FileWriter(doneFileName);
            for (int i = 0; i < todoList.size(); i++) {
                fw.write(todoList.indexOf(i));
            }
            fw.close();
        } catch (Exception e) {

        }

    }


    static String getDate() {
        Date date = new Date(System.currentTimeMillis());
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy/MM/dd");
        String s = formatter.format(date);
        return s;

    }

}
