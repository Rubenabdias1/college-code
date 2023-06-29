/*
The Basic Accounting Equation
what you have       =   where it came from
what you have       =   what you owe        +   what is yours free and clear
Economic resources  =   Claims on Resources
Economic resources  =   Outsider Claims     +   Owner Claims
Economic Resources  =   Creditor's Equities +   Owner's Equity
    Assets          =       Liabilities     +   Owner's Equity


*/
export const computeAssets = (
  liabilities: Liability[],
  ownerEquity: Equity[]
) => {
  //   return liabilities + ownerEquity;
};

/*

*/
// Assets are resources a comapny owns or controls
/*
Cash
Accounts Receivable		amounts owed to us for goods/services sold on credit
Note Receivable		promissory note
Prepaid Expenses		prepayments of future expenses
Inventory
Supplies 
Land
Buildings
Equipment

*/
class Asset {
  value: number;
}
// A receivable is an asset that promises
class Receivable extends Asset {}
// Liabilities are creditor's claims on assets.
/*
Accounts Payable	amounts owed to creditors for goods/services bought on credit
Notes Payable		money borrowed from banks
Wages Payable	wages owed to employees
Unearned Revenue	money already collected, but still “owe” something to our customer (we have not yet “earned”)
Taxes Payable
*/

/*
Increases in owner’s equity resulting from the operation of the business.

Increases in assets resulting from sales of a product or service in the normal course of business.
		Revenue
		Sales Revenue	
		Sales
		Fees Earned
		Commissions Earned

*/
class Revenue {}

/*
Decreases in owner’s equity that result from operating a business.

Cost of assets consumed or services used in the process of generating revenues.
		Rental Expense			Utilities Expense
		Wages Expense			Supplies Expense
		Salaries Expense		Advertising Expense
		Commissions Expense

*/
class Expense {}

class Liability {}
// A Payable is a liability that promises a future outflow of resources
class Payable extends Liability {}

// Equity is the owner's claim on assets. Also called net assets or residual equity.
/*
Net Assets Owner’s Equity = Assets – Liabilities
If Corporation, will have:	Stock
							Retained Earnings
							Dividends 

If not a Corporation:		Initial Investment
							Additional Investment (Contributions)
							Net Income
							Net Loss
							Withdrawals (instead of Dividends)

*/
class Equity extends Asset {}

class Transaction {}
