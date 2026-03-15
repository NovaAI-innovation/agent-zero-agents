## Example Blueprints (Optional)
Use these as structure references. Adapt to the user niche and requirements; do not copy verbatim.

### Example 1: Creator Content OS
**Target Buyer**
Solo creator publishing across newsletter, YouTube, and X.

**Core Outcome**
Consistent publishing cadence with a clear idea-to-publish pipeline.

**Page Tree**
- Home Dashboard
- Content Pipeline
- Idea Vault
- Content Calendar
- Assets Library
- KPI Review
- SOPs

**Databases**
- `Content Items`
  - Properties: `Title` (title), `Platform` (multi-select), `Status` (select), `Owner` (people), `Draft Date` (date), `Publish Date` (date), `Priority` (select), `Source Idea` (relation), `Campaign` (relation), `Word Count` (number), `CTA Added` (checkbox), `Days to Publish` (formula).
  - Views: Kanban by `Status`, Calendar by `Publish Date`, Table for backlog, "Due This Week".
- `Ideas`
  - Properties: `Idea` (title), `Theme` (multi-select), `Source` (select), `Effort` (select), `Linked Content` (relation), `Score` (formula).
  - Views: Inbox, Top Scored, Theme Groups.
- `Campaigns`
  - Properties: `Name` (title), `Goal` (text), `Start` (date), `End` (date), `Content Count` (rollup), `Published Count` (rollup), `Progress %` (formula).
  - Views: Active Campaigns, Timeline.

**Key Formula Notes**
- `Days to Publish`: dateBetween(prop("Publish Date"), now(), "days")
- `Score`: combines effort + theme priority heuristics.

**UX Notes**
- Home dashboard has "Today", "This Week", and one-click "New Content".
- Empty-state helper cards explain first 3 setup actions.

### Example 2: Freelancer Client Delivery Pipeline
**Target Buyer**
Freelancer or small agency handling multiple client projects.

**Core Outcome**
Track leads, proposals, active projects, deliverables, invoices, and follow-ups in one system.

**Page Tree**
- Agency Dashboard
- CRM
- Projects
- Deliverables
- Invoices
- Meetings & Notes
- Templates & SOPs

**Databases**
- `Clients`
  - Properties: `Client` (title), `Stage` (select), `Industry` (select), `Primary Contact` (text), `Email` (email), `Active Projects` (rollup), `LTV` (rollup), `Health` (formula), `Last Touch` (date).
  - Views: Pipeline Board, Active Clients, At-Risk.
- `Projects`
  - Properties: `Project` (title), `Client` (relation), `Status` (select), `Start` (date), `Due` (date), `Budget` (number), `Paid` (number), `Margin %` (formula), `Deliverables` (relation), `Overdue` (formula).
  - Views: Active Board, Timeline, Due Soon.
- `Deliverables`
  - Properties: `Deliverable` (title), `Project` (relation), `Type` (select), `Owner` (people), `Status` (select), `Due` (date), `Ready to Send` (checkbox).
  - Views: By Project, Review Queue.
- `Invoices`
  - Properties: `Invoice #` (title), `Client` (relation), `Project` (relation), `Amount` (number), `Issued` (date), `Due` (date), `Paid?` (checkbox), `Days Late` (formula).
  - Views: Unpaid, Paid, Overdue.

**Key Formula Notes**
- `Overdue`: if(and(not prop("Status") == "Done", prop("Due") < now()), true, false)
- `Margin %`: if(prop("Budget") > 0, (prop("Budget") - prop("Paid")) / prop("Budget"), 0)

**UX Notes**
- Dashboard surfaces "Invoices Overdue", "Projects At Risk", and "Today Follow-ups".
- Client page template preloads meeting note structure and kickoff checklist.

### Example 3: Personal Finance Planner
**Target Buyer**
Individuals/families who want monthly planning and spending control.

**Core Outcome**
Set monthly budgets, track transactions, and monitor financial progress with low friction.

**Page Tree**
- Finance Home
- Monthly Budget
- Transactions
- Accounts
- Savings Goals
- Reports
- Setup Guide

**Databases**
- `Transactions`
  - Properties: `Transaction` (title), `Date` (date), `Account` (relation), `Category` (select), `Type` (select), `Amount` (number), `Month` (formula), `Recurring?` (checkbox), `Notes` (text).
  - Views: This Month, Needs Review, Recurring.
- `Budget Categories`
  - Properties: `Category` (title), `Monthly Budget` (number), `Transactions` (relation), `Spent` (rollup), `Remaining` (formula), `% Used` (formula), `Status` (formula).
  - Views: Budget Board by `Status`, Top Overspend.
- `Accounts`
  - Properties: `Account` (title), `Type` (select), `Institution` (text), `Balance` (number), `Last Updated` (date).
  - Views: Cashflow Accounts, Credit Accounts.
- `Savings Goals`
  - Properties: `Goal` (title), `Target` (number), `Current` (number), `Deadline` (date), `Progress %` (formula), `On Track` (formula).
  - Views: Goal Progress, Deadline Timeline.

**Key Formula Notes**
- `% Used`: if(prop("Monthly Budget") > 0, prop("Spent") / prop("Monthly Budget"), 0)
- `Remaining`: prop("Monthly Budget") - prop("Spent")
- `Status`: if(prop("% Used") > 1, "Over", if(prop("% Used") > 0.8, "Watch", "OK"))

**UX Notes**
- Home page includes monthly snapshot cards and quick-add transaction button.
- Setup guide includes category defaults and account setup checklist.
