Title: Clojure Notes 1
Date: 2019-02-19
Category: Programming
Tags: books, code
Slug: clojure-notes-1
Author: Prasanna Venkadesh


Started learning another general purpose programming language called **[Clojure](https://clojure.org/)** which speaks **lisp** dialect and runs on top of **JVM**. Thanks to Kamalavelan for creating an interest for me to learn clojure and particularly the book titled, **[Clojure For The Brave and True](https://nostarch.com/clojure)** by David Higginbotham is very enjoyable.
https://nostarch.com/clojure
As a matter of taking notes of what I learn from the book, I share the notes here chapter wise.


### Chapter 1

1. Installing Clojure.
2. Installing [leiningen](https://leiningen.org/).
3. `lein new app <folder-name>`
4. `()` based syntax, namespaces, -main function, `println`
5. `lein run` => to build and see the output
6. `lein uberjar` => to build standalone jars
7. `lein repl` => to start a repl

### Chapter 2 - Emacs

1. I have largely ignored emacs tutorial.
2. But installed gnu emacs.
3. Downloaded clojure configuration for emacs
4. Downloaded and installed [Nightcode IDE](https://sekao.net/nightcode/) for clojure and I prefer it for now.
5. Also using lein repl to practice.

### Chapter 3 - Language Fundamentals

1. started using NightCode with REPL.
2. `FORMS` are expressions that clojure evaluates to produce a value.
3. ex: `1 "a string" ["a" "string" "vector]`
4. basic syntax: `(operator operand1 operand2 ... operandn)`
5. the above syntax is unifrom throughout LISP dialect.
6. `(str "string1" "string2)` => string1string2 => concatenates strings.
7. control flow => if do when
8. `(if boolean-form then-form optional-else-form)`

        (if true
	    "Sucess"
	    "Failure")

9. note that if..else can execute only one form. to overcome this we can use do.

        (if true
            (do (println "Success")
                "succesS")
            (do (println "Failure")
                "failure"))

10. `when` operator is like both if and do together but without else part and returns nil when the condition is false.

11. `or` and `and` boolean operators.
12. `nil` represents no value in clojure.
13. binding value to variables are done using **def** keyword

        (def name "prasanna")

14. ratio can be directly represented in clojure. `1/5`
15. **Maps** are key, value store. **Hashmap** and **Sorted maps** are present in clojure.

        (def sampleMap {:first_name "Prasanna" :last_name "Venkadesh})
        (get sampleMap :first_name)
        (sampleMap :first_name)
        (:first_name sampleMap)

        (def sampleHashMap (hashmap :a 1 :b 2))

16. Maps can also be nested and `get-in` function is used to retreive nested map values.

        (get-in {:a 0 :b {:c "1}} [:b :c])

17. **Vectors** are like 0 indexed arrays and can be heterogenous.

        [1 2 3 4]
        (def vecData [1 2 3 4])
        (get vecData 2)
        (conj vecData 10)

18. `conj` function is used to append value at to vector and `vector` function is used to create a new vector with supplied values.

        (vector "test" 1 "testing")

19. **list** in clojure is similar to vector, but `get` function will not work with list. `nth` function has to be used instead.

        '(1 2 3 4)
        (list 1 2 3 4)
        (def listData '(1 2 3 4))
        (def listData (list 1 2 3 4))
        (nth listData 0)

20. `conj` function with list will add elements to the **beginning** of the list.

        (conj listData 10)

21. Fetching elements from list using `nth` function will be slower than `get` in vector. When to use what depends on whether we want to add elements to end or beginning of the data structure.
22. Clojure supports **higher-order functions**, i.e a function that can take another function as argument or can return another function. Programming languages with higher-order functions are said to support **first class functions** because we can treat functions as values in the same way we treat other data types like number, string, etc., 

23. **inc** function can increment a numeric value. **map** function can operate over a collection and can return a list as result.

        (inc 20)
        (map inc [1 2 3 4])

24. **[]** is used to pass arguments to functions. function parameters can be used to overload and can be used for multiple purposes. Those are called **Arity**.

        (defn myFunction
          ([]
            (println "no arguments supplied"))
          ([x, y])
            (println "two arguments supplied"))
        )

25. `&` ampresand is used to denote rest of parameters. Like \*args in `python`

        (defn myFunction
          [name]
	  (str "Hi. I am " name))

        (defn myFunc
          [& names]
          (map myFunc names))

        (myFunc "Prasanna" "Kamal")

26. **Anonymous Functions** are functions without names. They can be defined anywhere using `fn` keyword.

        (fn [arguments] function-body)

        ((fn [x] (* x 3)) 8)

        (map (fn [name] (str "Hi " name) ["Prasanna" "Kamal"])

27. anonymous functions can also be bound to variables.

        (def my-function (fn [name] (str "Hi, " name)))
        (my-function "Prasanna")

28. There is a much more shortcut way to define anonymous functions using `#`.

        #(+ % 2)
        (#(+ % 2) 8)
        (#(str "Hi " %) "Prasanna")

29. If the anonymous function takes multiple arguments, then `%1 %2 ... %n` form can be used.

30. **Destructuring** is about binding names to values in a collection based on positions.

        (defn chooser
          [[first-param]]
          first-param)

        (chooser ["Prasanna" "Kamal"])

        (defn chooser
          [[name age & other]]
          (println (str "Hi, " name))
          (println (str "Your age: " age))
          (prinln (str "Other info: " (clojure.string/join ", " other))))
   
        (chooser ["Prasanna" 28 "test@testing.org" "B+"])

31. Clojure has **closures**. Yes. closures are those functions that are returned by another functions. closure by itself is a design pattern to indicate state maintanence or scope of variables. To be frank, I haven't grasped this design well yet.

        (defn inc-maker
          "Create a custom incrementor"
          [inc-by]
          #(+ % inc-by))

        (def inc3 (inc-maker 3))

        (inc3 7)

End of Chapter 3. Will continue further notes in separate post.
