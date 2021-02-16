//B.11 Pg 471
public class GradeBook {
    private String courseName;
    private String instructor;

    public GradeBook(String name, String instructor) {
        this.courseName = name;
        this.instructor = instructor;
    }

    public void setInstructor(String instructor) {
        this.instructor = instructor;
    }

    public void setCourseName(String name) {
        this.courseName = name;
    }

    public String getInstructor() {
        return this.instructor;
    }

    public String getCourseName() {
        return this.courseName;
    }

    public void displayMessage() {
        System.out.printf( "Welcome to the grade book for: %s!\n" +
            "This course is presented by: %s!",
            getCourseName(), getInstructor() );
    }
}