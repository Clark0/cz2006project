package sg.edu.ntu.e.fang0074.ipet;

/**
 * Created by user on 15/3/2018.
 */

public class ClinicItem {
    private String name;
    private int photo;
    private int phone;
    private String rating;

    public ClinicItem(String name, int photo, int phone, String rating) {
        this.name = name;
        this.photo = photo;
        this.phone = phone;
        this.rating = rating;
    }

    public String getName() {
        return name;
    }

    public int getPhone(){return phone;}

    public String getRating() {
        return rating;
    }

    public int getPhoto() {
        return photo;
    }

    public void setName(String name) {
        this.name = name;
    }
    public void setPhone(int phone){this.phone = phone;}
    public void setRating(String rating) {this.rating = rating;}
    public void setPhoto(int photo) {
        this.photo = photo;
    }
}
