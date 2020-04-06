import java.io.*;
import java.util.Scanner;

class datefile {

    private Scanner x;
    public void openFile(String fileName) {
        try {
            x = new Scanner(new File(fileName));
        } catch (Exception e) {
            System.out.println("File was not found!");
        }
    }

    public void readFile() {
        while (x.hasNext()) {
            String date = x.next();
            date.trim();

            System.out.println(calcDate(date));
        }
    }

    public static boolean isLeap(int year) {
        return (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0));
    }

    public static boolean isValidDate(int month, int day, int year) {

        if (year < 1800 || year > 2020)
            return false;
        if (month < 1 || month > 12)
            return false;
        if (day < 1 || day > 31)
            return false;

        if (month == 2) {
            if (isLeap(year)) {
                if (day > 29) {
                    return false;
                }
            } else {
                if (day > 28) {
                    return false;
                }
            }
        }

        if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) {
                return false;
            }
        }
        return true;
    }

    public static String calcDate(String date) {

        String monthstring = date.substring(0, 2);
        int month = Integer.parseInt(monthstring);

        String dayName = date.substring(3, 5);
        int day = Integer.parseInt(dayName);

        String yearName = date.substring(6, 10);
        int year = Integer.parseInt(yearName);

        if (isValidDate(month, day, year)) {

            String months[] = { "January", "February", "March", "April", "May", "June", "July", "August", "September",
                    "October", "November", "December" };
            String monthName = months[month - 1];

            String weekdays[] = { "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" };

            int t[] = { 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 };
            if (month < 3) {
                year -= 1;
            }
            int weekdayIndex = (year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7;
            String weekday = weekdays[weekdayIndex];

            return weekday + ", " + monthName + " " + dayName + ", " + yearName;

        } else {

            return date + " is NOT a valid date.";
        }
    }

    public void closeFile() {
        x.close();
    }
}

class main {

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        System.out.println("Enter fileName: ");
        String fileName = s.nextLine();

        datefile dateFile = new datefile();

        dateFile.openFile(fileName);
        dateFile.readFile();
        dateFile.closeFile();
    }
}