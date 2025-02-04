CREATE TABLE Employees (
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    HireDate DATE,
    Email VARCHAR(100)
);

INSERT INTO Employees (FirstName, LastName, HireDate, Email) VALUES
('John', 'Doe', '2023-01-15', 'john.doe@example.com'),
('Jane', 'Smith', '2023-02-20', 'jane.smith@example.com'),
('Emily', 'Johnson', '2023-03-10', 'emily.johnson@example.com');