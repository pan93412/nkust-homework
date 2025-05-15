from dataclasses import dataclass
import numpy_financial as npf

@dataclass
class AnalyzedResult:
    name: str
    npv: float
    irr: float
    mirr: float

    def __str__(self):
        return f"{self.name} Project Analysis Results:\nNPV: {self.npv:,.2f}\nIRR: {self.irr * 100:.2f}%\nMIRR: {self.mirr * 100:.2f}%"

class Project:
    """Class representing a capital investment project with cash flows."""
    
    def __init__(self, name: str, cash_flows: list[float], discount_rate: float):
        """
        Initialize a project with its name, cash flows and discount rate.
        
        Args:
            name: The project identifier
            cash_flows: List of cash flows starting with initial investment (negative)
            discount_rate: Rate used for present value calculations
        """
        self.name = name
        self.cash_flows = cash_flows
        self.discount_rate = discount_rate
    
    def calculate_npv(self) -> float:
        """Calculate the Net Present Value (NPV) of the project."""
        return npf.npv(self.discount_rate, self.cash_flows)
    
    def calculate_irr(self) -> float:
        """Calculate the Internal Rate of Return (IRR) of the project."""
        return npf.irr(self.cash_flows)
    
    def calculate_mirr(self, reinvestment_rate: float) -> float:
        """
        Calculate the Modified Internal Rate of Return (MIRR) of the project.
        
        Args:
            reinvestment_rate: Rate at which positive cash flows are reinvested
        """
        n = len(self.cash_flows)
        positive_flows = [cf if cf > 0 else 0 for cf in self.cash_flows]
        negative_flows = [cf if cf < 0 else 0 for cf in self.cash_flows]
        
        # Present value of negative cash flows
        pv_neg = npf.npv(self.discount_rate, negative_flows)
        
        # Future value of positive cash flows
        fv_pos = sum([cf * (1 + reinvestment_rate)**(n - i - 1) 
                      for i, cf in enumerate(positive_flows)])
        
        return (abs(fv_pos / pv_neg))**(1 / (n - 1)) - 1


class CapitalBudgetingAnalyzer:
    """Class for analyzing multiple capital investment projects."""
    
    def __init__(self, discount_rate: float = 0.10, reinvestment_rate: float = 0.10):
        """
        Initialize the analyzer with discount and reinvestment rates.
        
        Args:
            discount_rate: Rate used for NPV calculations
            reinvestment_rate: Rate used for MIRR calculations
        """
        self.discount_rate = discount_rate
        self.reinvestment_rate = reinvestment_rate
        self.projects: list[Project] = []
    
    def add_project(self, name: str, cash_flows: list[float]) -> None:
        """
        Add a project to the analyzer.
        
        Args:
            name: Project identifier
            cash_flows: List of cash flows starting with initial investment
        """
        project = Project(name, cash_flows, self.discount_rate)
        self.projects.append(project)
    
    def analyze_project(self, project: Project) -> AnalyzedResult:
        """
        Analyze a single project and return metrics.
        
        Args:
            project: The project to analyze
            
        Returns:
            AnalyzedResult object containing NPV, IRR, and MIRR values
        """
        npv = project.calculate_npv()
        irr = project.calculate_irr()
        mirr = project.calculate_mirr(self.reinvestment_rate)
        
        return AnalyzedResult(project.name, npv, irr, mirr)

    def analyze_all_projects(self) -> list[AnalyzedResult]:
        """Analyze and print results for all added projects."""
        return [self.analyze_project(project) for project in self.projects]
    
    def get_best_project(self) -> AnalyzedResult | None:
        """
        Identify the best project based on NPV.
        
        Returns:
            AnalyzedResult object with highest NPV or None if no projects exist
        """
        if not self.projects:
            return None
        return max(self.projects, key=lambda p: p.calculate_npv())

# Main execution
if __name__ == "__main__":
    # Create analyzer with default rates
    analyzer = CapitalBudgetingAnalyzer(discount_rate=0.1175, reinvestment_rate=0.1175)
    
    # Add projects with their cash flows (in dollars)
    analyzer.add_project("A", [-5500000, 950000, 1350000, 1500000, 1800000, 1950000, 2100000])
    analyzer.add_project("B", [-7700000, 1250000, 1900000, 2550000, 2700000, 2350000, 2250000])
    
    # Analyze all projects
    results = analyzer.analyze_all_projects()
    for result in results:
        print(result)
        print("---\n")
    
    # Find the best project based on NPV
    best_project = analyzer.get_best_project()
    if best_project:
        print(f"Based on NPV analysis, the recommended project is: {best_project.name}")
