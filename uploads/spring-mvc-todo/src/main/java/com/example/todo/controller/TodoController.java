package com.example.todo.controller;

import com.example.todo.model.Todo;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.Arrays;

@Controller
public class TodoController {
    @GetMapping("/")
    public String todoList(Model model) {
        model.addAttribute("todos", Arrays.asList(new Todo(1L, "Sample task", false)));
        return "todo";
    }
}
