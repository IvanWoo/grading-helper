function finaltestfun()
    import matlab.unittest.TestSuite;
    suiteClass = TestSuite.fromClass(?hw1UnitTest);

    maindir = '../hw1/'; % maindir is the address where the assignments store
    subdir  = dir(maindir);

    % http://blog.csdn.net/u012675539/article/details/43671663
    for i = 1 : length( subdir )
        % skip invalid subfolder
        if(isequal(subdir(i).name, '.')||...
           isequal(subdir(i).name, '..')||...
           ~subdir(i).isdir)
           continue;
        end

        subdirpath = fullfile( maindir, subdir(i).name);

        cd(subdirpath);

        % skip the assignments already are garded in consideration of performance
        if exist('hw1_results.csv', 'file') == 2
            continue;
        end

        result = run(suiteClass);
        rt = table(result);
        writetable(rt,'hw1_results.csv','QuoteStrings',true);

        cd('..'); % back to maindir
    end
end