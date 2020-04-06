import java.util.Scanner;

class Book {

  private int stock_number;
  private String author;
  private String title;
  private int price;
  private int number_of_pages;

  public int getStockNumber() {
    return this.stock_number;
  }

  public String getAuthor() {
    return this.author;
  }

  public String getTitle() {
    return this.title;
  }

  public int getPrice() {
    return this.price;
  }

  public int getNumberOfPages() {
    return this.number_of_pages;
  }

  public void setStockNumber(int stock_number) {
    this.stock_number = stock_number;
  }

  public void setAuthor(String author) {
    this.author = author;
  }

  public void setTitle(String title) {
    this.title = title;
  }

  public void setPrice(int price) {
    this.price = price;
  }

  public void setNumberOfPages(int number_of_pages) {
    this.number_of_pages = number_of_pages;
  }
}

class c {

  public static void main(String[] args) {

    Book books[] = new Book[10];

    Scanner s = new Scanner(System.in);

    for (int i = 1; i <= books.length; i++) {

      System.out.println("\n### Book number: " + i + " ###");

      System.out.println("Enter stock number: ");
      int stock_number = s.nextInt();
      s.nextLine();

      System.out.println("Enter author: ");
      String author = s.nextLine();

      System.out.println("Enter title: ");
      String title = s.nextLine();

      System.out.println("Enter price: ");
      int price = s.nextInt();
      s.nextLine();

      System.out.println("Enter number of pages: ");
      int number_of_pages = s.nextInt();
      s.nextLine();

      Book book = new Book();

      book.setStockNumber(stock_number);
      book.setAuthor(author);
      book.setTitle(title);
      book.setPrice(price);
      book.setNumberOfPages(number_of_pages);

      books[i - 1] = book;
    }

    for (int i = 0; i < books.length; i++) {

      int n = i + 1;
      System.out.println("\n### Book number: " + n + " ###");

      System.out.println("stock number: " + books[i].getStockNumber());
      System.out.println("author: " + books[i].getAuthor());
      System.out.println("title: " + books[i].getTitle());
      System.out.println("price: " + books[i].getPrice());
      System.out.println("number of pages: " + books[i].getNumberOfPages());
    }
  }
}
