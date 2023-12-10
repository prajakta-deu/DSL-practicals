#include <iostream>
using namespace std;
#define SIZE 5
class Dequeue
{
    int a[10], front, rear, count;
public:
    Dequeue()
    {
        front = -1;
        rear = -1;
        count = 0;
    }
    void addBegin(int item)
    {
        int i;
        if (front == -1)
        {
            front++;
            rear++;
            a[rear] = item;
            count++;
        }
        else if (rear >= SIZE - 1)
        {
            cout << "\nInsertion is not possible,overflow!!!!";
        }
        else
        {
            for (i = count; i >= 0; i--)
            {
                a[i] = a[i - 1];
            }
            a[i] = item;
            count++;
            rear++;
        }
    }
    void addEnd(int item)
    {
        if (front == -1)
        {
            front++;
            rear++;
            a[rear] = item;
            count++;
        }
        else if (rear >= SIZE - 1)
        {
            cout << "\nInsertion is not possible,overflow!!!";
            return;
        }
        else
        {
            a[++rear] = item;
        }
    }
    void deleteFront()
    {
        if (front == -1)
        {
            cout << "Deletion is not possible:: Dequeue is empty";
            return;
        }
        else
        {
            if (front == rear)
            {
                front = rear = -1;
                return;
            }
            cout << "The deleted element is " << a[front];
            front = front + 1;
        }
    }
    void deleteEnd()
    {
        if (front == -1)
        {
            cout << "Deletion is not possible:Dequeue is empty";
            return;
        }
        else
        {
            if (front == rear)
            {
                front = rear = -1;
            }
            cout << "The deleted element is " << a[rear];
            rear = rear - 1;
        }
    }
    void display()
    {
        for (int i = front; i <= rear; i++)
        {
            cout << a[i] << " ";
        }
    }
};
int main()
{
    int c, item;
    Dequeue d1;

    do
    {
        cout << "\n\n****DEQUEUE OPERATION****\n";
        cout << "\n1-Insert at beginning";
        cout << "\n2-Insert at end";
        cout << "\n3-Display";
        cout << "\n4-Deletion from front";
        cout << "\n5-Deletion from rear";
        cout << "\n6-Exit";
        cout << "\nEnter your choice<1-6>:";
        cin >> c;

        switch (c)
        {
        case 1:
            cout << "Enter the element to be inserted:";
            cin >> item;
            d1.addBegin(item);
            break;
        case 2:
            cout << "Enter the element to be inserted:";
            cin >> item;
            d1.addEnd(item);
            break;
        case 3:
            d1.display();
            break;
        case 4:
            d1.deleteFront();
            break;
        case 5:
            d1.deleteEnd();
            break;
        case 6:
            exit(1);
            break;
        default:
            cout << "Invalid choice";
            break;
        }
    } while (c != 7);
    return 0;
}