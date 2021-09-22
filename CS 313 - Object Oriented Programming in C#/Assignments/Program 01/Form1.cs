/*
 * Ruben Nunez
 * CS 313 01
 * Program Assignment 01
 * Wednesday, September 22, 2021
 * This program contains images of the numbers from 1 to 5. If an user clicks
 * any of the numbers, it is going to show a message box containing the english
 * spelling of the number that was clicked.
*/

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Program_01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void numberOnePictureBox_Click(object sender, EventArgs e)
        {
            MessageBox.Show("One");
        }

        private void numberTwoPictureBox_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Two");
        }

        private void numberThreePictureBox_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Three");
        }

        private void numberFourPictureBox_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Four");
        }

        private void numberFivePictureBox_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Five");
        }
    }
}
