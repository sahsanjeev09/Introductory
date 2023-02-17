import java.util.ArrayList;
import java.util.Scanner;

public class MergeSort_SanjeevKumarSah2329256 {

    public static void getInput(ArrayList<Integer> al) {
        //Input Function To Take Input From The User
        Scanner sc = new Scanner(System.in);
        System.out.print(" Enter The Number of Digits That You Want To Enter: ");
        int i = sc.nextInt();


        // Print The OutPut In Reference To Line Spacing
        System.out.println();
        System.out.println("Enter The Digits That You Want To Arrange: ");

        for (int j = 0; j < i; j++) {
            al.add(sc.nextInt());
        }
        System.out.println();
        System.out.print("The Digits That You Have Entered Are: ");

        System.out.println(al);
        System.out.println();
    }

    public static void getOutput(ArrayList<Integer> al) {
        //Output Function To Show The Output For The User
        System.out.print("The Sorted List From The Array List Are: ");
        for (int i = 0; i < al.size(); i++) {
            System.out.print("[" + al.get(i) + "]");

        }
    }

    public static void merge(ArrayList<Integer> al, int beg, int mid, int end) {
        //Implementing MergeSort By Dividing Digits Into Two Part And Sorting It Accordingly


        int i = beg;
        int j = mid + 1;
        int k = end;
        if ((k - i) >= 2) {
            while (i <= j && i <= k) {
                if (al.get(i) > (al.get(j))) {
                    al.add(i, al.remove(j));
                    i++;
                    j++;
                } else if (al.get(i) == al.get(j)) {
                    al.add(i, al.remove(j));
                    i++;
                    j++;
                } else {
                    i++;
                }
            }

        } else {
            if (k > i) {
                if (al.get(i) > al.get(k)) {
                    int endVarraylstue = al.remove(k);
                    al.add(i, endVarraylstue);
                }
            }
        }
    }

     void sort(ArrayList<Integer> al, int beg, int end) {
        //Using Merge Sort To Combine The Sorted Digit
        if (beg < end) {
            int mid = (beg + end) / 2;
            sort(al, beg, mid);
            sort(al, mid + 1, end);
            merge(al, beg, mid, end);
        }
    }

     void main(String[] args) {

//        Main Function Where Welcome Message Is Shown
        System.out.println("                                 ");
        System.out.println("Student Name : Sanjeev Kumar Sah");
        System.out.println("Student Number: 2329256");
        System.out.println("                                 ");
        System.out.println("Let's Perform Sorting By Using Merge Sort");
        System.out.println("                                         ");
        ArrayList<Integer> al = new ArrayList<>();
        getInput(al);
        sort(al, 0, al.size() - 1);
        getOutput(al);
    }
}