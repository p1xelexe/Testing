package org.example;

import static org.junit.Assert.*;
import org.junit.Test;

import javax.json.*;
import java.io.IOException;
import java.io.StringReader;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Main {

    public static HttpResponse<String> getResponse(String Url) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request_get = HttpRequest.newBuilder()
                .uri(URI.create(Url))
                .header("Content-Type", "application/json")
                .GET()
                .build();

        return client.send(request_get, HttpResponse.BodyHandlers.ofString());
    }
    public static String end_testing(String num){
        return "[Конец " + num + " кейса, все прошло хорошо]\n";
    }

    public static String start_testing(String num){
        return "[Начало " + num + " кейса]";
    }

    @Test
    public void test_first_case() throws IOException, InterruptedException {
        String Url = "https://dog.ceo/api/breeds/list/all";
        String num = "первого";
        System.out.println(start_testing(num));
        HttpResponse<String> response = getResponse(Url);

        // Проверка статуса ответа (HTTP 200 OK)
        assertEquals(response.statusCode(), 200);

        // Попытка разобрать JSON-строку в объект JSON
        try (JsonReader jsonReader = Json.createReader(new StringReader(response.body()))) {
            JsonObject jsonObject = jsonReader.readObject();

            // Проверка наличия поля "message"
            assertTrue(jsonObject.containsKey("message"));

            // Проверка типа поля "message"
            JsonValue messageValue = jsonObject.get("message");
            assertEquals(JsonValue.ValueType.OBJECT, messageValue.getValueType());

            // Проверка, что "message" не пустое
            assertFalse(messageValue.asJsonObject().isEmpty());
        } catch (Exception e) {
            e.printStackTrace();
            fail("Failed testing");
        }
        System.out.println(end_testing(num));
    }

    @Test
    public void test_second_case() throws IOException, InterruptedException {
        String Url = "https://dog.ceo/api/breeds/image/random";
        String num = "второго";
        System.out.println(start_testing(num));
        HttpResponse<String> response = getResponse(Url);

        // Проверка статуса ответа (HTTP 200 OK)
        assertEquals(response.statusCode(), 200);

        // Попытка разобрать JSON-строку в объект JSON
        try (JsonReader jsonReader = Json.createReader(new StringReader(response.body()))) {
            JsonValue jsonString = jsonReader.readValue();

            assertTrue(jsonString.toString().contains("message")); // Проверка наличия "message"
            assertFalse(jsonString.toString().isEmpty()); // Проверка того что, "message" не пуста

        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Failed testing");
        }
        System.out.println(end_testing(num));
    }

    @Test
    public void test_third_case() throws IOException, InterruptedException {
        String Url = "https://dog.ceo/api/breed/hound/list";
        String num = "третьего";
        System.out.println(start_testing(num));
        HttpResponse<String> response = getResponse(Url);

        // Проверка статуса ответа (HTTP 200 OK)
        assertEquals(response.statusCode(), 200);
        try (JsonReader jsonReader = Json.createReader(new StringReader(response.body()))) {
            JsonObject jsonObject = jsonReader.readObject();

            // Проверка наличия поля "message"
            assertTrue(jsonObject.containsKey("message"));

            // Проверка типа поля "message"
            JsonValue messageValue = jsonObject.get("message");
            assertEquals(JsonValue.ValueType.ARRAY, messageValue.getValueType());

            // Проверка, что "message" не пустое
            assertFalse(messageValue.asJsonArray().isEmpty());

            System.out.println(end_testing(num));
        } catch (Exception e){
            e.printStackTrace();
            System.out.println("Failed testing");
        }
    }

    @Test
    public void test_fourth_case() throws IOException, InterruptedException {
        String Url = "https://dog.ceo/api/breed/hound/afghan/images";
        String num = "четвертого";
        System.out.println(start_testing(num));
        HttpResponse<String> response = getResponse(Url);

        // Проверка статуса ответа (HTTP 200 OK)
        assertEquals(response.statusCode(), 200);

        try (JsonReader jsonReader = Json.createReader(new StringReader(response.body()))) {
            JsonObject jsonObject = jsonReader.readObject();

            // Проверка наличия поля "message"
            assertTrue(jsonObject.containsKey("message"));

            // Проверка типа поля "message"
            JsonValue messageValue = jsonObject.get("message");
            assertEquals(JsonValue.ValueType.ARRAY, messageValue.getValueType());

            // Проверка, что "message" не пустое
            assertFalse(messageValue.asJsonArray().isEmpty());
            System.out.println(end_testing(num));
        }catch (Exception e){
            e.printStackTrace();
            System.out.println("Failed testing");
        }
    }

    @Test
    public void test_fifth_case() throws IOException, InterruptedException {
        String Url = "https://dog.ceo/api/breed/hound/afghan/images/random";
        String num = "пятого";
        System.out.println(start_testing(num));
        HttpResponse<String> response = getResponse(Url);

        assertEquals(response.statusCode(), 200);

        try (JsonReader jsonReader = Json.createReader(new StringReader(response.body()))) {
            JsonValue jsonString = jsonReader.readValue();

            assertTrue(jsonString.toString().contains("message")); // Проверка наличия "message"
            assertFalse(jsonString.toString().isEmpty()); // Проверка того что, "message" не пуста

            System.out.println(end_testing(num));
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Failed testing");
        }
    }

    public static void main(String[] args){
        System.out.println("\nПроверка завершена");
    }
}
