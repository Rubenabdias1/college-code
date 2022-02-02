using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
/*
Ruben Nunez
CS 313 01
Program 04 Chapter 04
Monday, November 8, 2021
This program displays a menu with burger choices, three sizes of fries
and two options for drinks. When the user clicks compute, the program
will add up the prices of the items selected and display the bill.
*/

namespace Assign04Chapter_04
{
    public partial class Form1 : Form
    {
        const decimal REGULAR_BURGER_PRICE = 4.19m;
        const decimal CHEESEBURGER_PRICE =  4.79m;
        const decimal BACON_BURGER_PRICE = 4.79m;
        const decimal BACON_CHEESEBURGER_PRICE = 5.39m;

        const decimal SMALL_FRIES_PRICE = 2.39m;
        const decimal MEDIUM_FRIES_PRICE = 3.09m;
        const decimal LARGE_FRIES_PRICE = 4.99m;

        const decimal SODA_PRICE = 1.69m;
        const decimal BOTTLED_WATER_PRICE = 1.49m;

        public Form1()
        {
            InitializeComponent();
        }

        private void computeButton_Click(object sender, EventArgs e)
        {
            decimal costOfMeal = 0;
            
            if (burgersCheckBox.Checked)
            {

                if (cheeseBurgerRadioButton.Checked ) 
                {
                    costOfMeal += CHEESEBURGER_PRICE;
                    outputListBox.Items.Add("Cheeseburger: ......... " + CHEESEBURGER_PRICE.ToString("C"));
                }
                else if (baconBurgerRadioButton.Checked)
                {
                    costOfMeal += BACON_BURGER_PRICE;
                    outputListBox.Items.Add("w/ Bacon: ............. " + BACON_CHEESEBURGER_PRICE.ToString("C"));
                }
                else if (baconCheeseBurgerRadioButton.Checked) 
                {
                    costOfMeal += BACON_CHEESEBURGER_PRICE;
                    outputListBox.Items.Add("Bacon CheeseBurger: ... " + BACON_CHEESEBURGER_PRICE.ToString("C"));

                }
                else
                {
                    costOfMeal += REGULAR_BURGER_PRICE;
                    outputListBox.Items.Add ("Regular Burger: ....... " + REGULAR_BURGER_PRICE.ToString("C"));

                }
            }
            
            if (friesCheckBox.Checked)
            {
                if (mediumFriesRadioButton.Checked)
                {
                    costOfMeal += MEDIUM_FRIES_PRICE;
                    outputListBox.Items.Add("Medium Fries:.......... " + MEDIUM_FRIES_PRICE.ToString("C"));


                }
                else if (largeFriesRadioButton.Checked)
                {
                    costOfMeal += LARGE_FRIES_PRICE;
                    outputListBox.Items.Add("Large Fries: .......... " + LARGE_FRIES_PRICE.ToString("C"));

                }
                else
                {
                    costOfMeal += SMALL_FRIES_PRICE;
                    outputListBox.Items.Add("Small Fries: .......... " + SMALL_FRIES_PRICE.ToString("C"));

                }
            }

            if (drinksCheckBox.Checked) {
                
                if (bottledWaterRadioButton.Checked)
                {
                    costOfMeal += BOTTLED_WATER_PRICE;
                    outputListBox.Items.Add("Bottled Water: ........ " + BOTTLED_WATER_PRICE.ToString("C"));
                }
                else
                {
                    costOfMeal += SODA_PRICE;
                    outputListBox.Items.Add("Soda: ................. " + SODA_PRICE.ToString("C"));

                }
            }
;
        }


        private void burgersCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            burgersChoicesGroupBox.Visible = burgersCheckBox.Checked;
        }

        private void friesCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            friesChoicesGroupBox.Visible = friesCheckBox.Checked;
        }

        private void drinksCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            drinksChoicesGroupBox.Visible = drinksCheckBox.Checked;
        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
        
        
    }
}
