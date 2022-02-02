using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
/*
 * Ruben Nunez
 * CS 313 01
 * Program Chapter 05
 * Monday, November 29, 2021
 * This game of Craps has the following rules:
•	The player will roll two dice
•	If the total is 2, 3, or 12, the player loses
•	If the total is 7 or 11, the player wins
•	If the total is any other number, that is the point and the player rolls until one of the following happens
    o	If the total is the point, the player wins
    o	If the total is a 7 or 11 the player loses
 * The program allows the user to play this game!
*/
namespace Chapter_05
{
    public partial class Form1 : Form
    {
        private int thePoint = 0;
        private StreamWriter outputFile;
        public Form1()
        {
            InitializeComponent();
            outputFile = File.CreateText("The Crab Game Rolls.txt");

        }

        private void rollDie1 (int value)
        {
            firstDie1PictureBox.Visible = false;
            firstDie2PictureBox.Visible = false;
            firstDie3PictureBox.Visible = false;
            firstDie4PictureBox.Visible = false;
            firstDie5PictureBox.Visible = false;
            firstDie6PictureBox.Visible = false;

            switch (value)
            {
                case 1:
                    firstDie1PictureBox.Visible = true;
                    break;
                case 2:
                    firstDie2PictureBox.Visible = true;
                    break;
                case 3:
                    firstDie3PictureBox.Visible = true;
                    break;
                case 4:
                    firstDie4PictureBox.Visible = true;
                    break;
                case 5:
                    firstDie5PictureBox.Visible = true;
                    break;
                case 6:
                    firstDie6PictureBox.Visible = true;
                    break;
            }
        }

        private void rollDie2(int value)
        {
            secondDie1PictureBox.Visible = false;
            secondDie2PictureBox.Visible = false;
            secondDie3PictureBox.Visible = false;
            secondDie4PictureBox.Visible = false;
            secondDie5PictureBox.Visible = false;
            secondDie6PictureBox.Visible = false;

            switch (value)
            {
                case 1:
                    secondDie1PictureBox.Visible = true;
                    break;
                case 2:
                    secondDie2PictureBox.Visible = true;
                    break;
                case 3:
                    secondDie3PictureBox.Visible = true;
                    break;
                case 4:
                    secondDie4PictureBox.Visible = true;
                    break;
                case 5:
                    secondDie5PictureBox.Visible = true;
                    break;
                case 6:
                    secondDie6PictureBox.Visible = true;
                    break;
            }

        }

        private void rollButton_Click(object sender, EventArgs e)
        {
            outputFile.WriteLine("Rolling the dices:");

            int points, die1, die2;
            Random rand = new Random();
            string output;

            die1 = rand.Next(1, 6);
            die2 = rand.Next(1, 6);

            rollDie1(die1);
            rollDie2(die2);

            points = die1 + die2;
            output = "You rolled: " + die1 + " and " + die2 + ". This sums up to " + points + ". ";

            if ((points == 2) || (points == 3) || (points == 12))
            {
                output += "You lost.";
                thePoint = 0;

            }
            else if (points == thePoint)
            {
                output += "This is the point! You lost.";
                thePoint = 0;
            }
            else if ((points == 7) || (points == 11))
            {
                output += "You won!";
                thePoint = 0;

            } else if (thePoint == 0)
            {
                 thePoint = points;
                 MessageBox.Show("The point is " + thePoint + ".");
                 outputFile.WriteLine("The point is " + thePoint);
             }
            
            MessageBox.Show(output);
            outputFile.WriteLine(output);

        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            this.Close();
            outputFile.Close();
        }
        
    }
}
